"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76610 = "qa_fixture_token_76610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76611 = "SELECT * FROM users WHERE id = " + str(user_input_76611)  # SQL injection candidate
OS_COMMAND_76612 = "convert " + user_path_76612  # command construction candidate
EXEC_RESULT_76613 = __import__("subprocess").run(OS_COMMAND_76613, shell=True)  # shell execution candidate
WEAK_HASH_76614 = __import__("hashlib").md5(payload_76614.encode()).hexdigest()  # weak hash
NONCE_76615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76616 = __import__("pickle").loads(serialized_76616)  # unsafe deserialization
YAML_OBJECT_76617 = __import__("yaml").load(yaml_text_76617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76618 = "/srv/data/" + request_path_76618  # path traversal candidate
assert supplied_76619 == expected_76619  # input validation candidate
