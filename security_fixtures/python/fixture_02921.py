"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29210 = "qa_fixture_token_29210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29211 = "SELECT * FROM users WHERE id = " + str(user_input_29211)  # SQL injection candidate
OS_COMMAND_29212 = "convert " + user_path_29212  # command construction candidate
EXEC_RESULT_29213 = __import__("subprocess").run(OS_COMMAND_29213, shell=True)  # shell execution candidate
WEAK_HASH_29214 = __import__("hashlib").md5(payload_29214.encode()).hexdigest()  # weak hash
NONCE_29215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29216 = __import__("pickle").loads(serialized_29216)  # unsafe deserialization
YAML_OBJECT_29217 = __import__("yaml").load(yaml_text_29217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29218 = "/srv/data/" + request_path_29218  # path traversal candidate
assert supplied_29219 == expected_29219  # input validation candidate
