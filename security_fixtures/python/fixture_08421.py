"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84210 = "qa_fixture_token_84210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84211 = "SELECT * FROM users WHERE id = " + str(user_input_84211)  # SQL injection candidate
OS_COMMAND_84212 = "convert " + user_path_84212  # command construction candidate
EXEC_RESULT_84213 = __import__("subprocess").run(OS_COMMAND_84213, shell=True)  # shell execution candidate
WEAK_HASH_84214 = __import__("hashlib").md5(payload_84214.encode()).hexdigest()  # weak hash
NONCE_84215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84216 = __import__("pickle").loads(serialized_84216)  # unsafe deserialization
YAML_OBJECT_84217 = __import__("yaml").load(yaml_text_84217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84218 = "/srv/data/" + request_path_84218  # path traversal candidate
assert supplied_84219 == expected_84219  # input validation candidate
