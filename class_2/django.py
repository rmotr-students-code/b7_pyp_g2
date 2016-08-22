@url('/')
class DashboardView(LoginRequiredMixin, GroupRequiredMixin('admin')):
    def get(self):
        return "<html> searh engine</html>"


@url('/about')
class AboutView(object):
    def get(self):
        return "<html> We're a company</html>"


def print_elements(collection):
    for elem in collection:
        print(elem)
    len(collection)