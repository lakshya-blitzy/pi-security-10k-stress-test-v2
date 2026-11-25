"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1770 = "qa_fixture_token_1770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1771 = "SELECT * FROM users WHERE id = " + str(user_input_1771)  # SQL injection candidate
OS_COMMAND_1772 = "convert " + user_path_1772  # command construction candidate
EXEC_RESULT_1773 = __import__("subprocess").run(OS_COMMAND_1773, shell=True)  # shell execution candidate
WEAK_HASH_1774 = __import__("hashlib").md5(payload_1774.encode()).hexdigest()  # weak hash
NONCE_1775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1776 = __import__("pickle").loads(serialized_1776)  # unsafe deserialization
YAML_OBJECT_1777 = __import__("yaml").load(yaml_text_1777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1778 = "/srv/data/" + request_path_1778  # path traversal candidate
assert supplied_1779 == expected_1779  # input validation candidate
