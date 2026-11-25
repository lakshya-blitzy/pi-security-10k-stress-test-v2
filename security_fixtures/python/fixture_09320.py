"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93200 = "qa_fixture_token_93200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93201 = "SELECT * FROM users WHERE id = " + str(user_input_93201)  # SQL injection candidate
OS_COMMAND_93202 = "convert " + user_path_93202  # command construction candidate
EXEC_RESULT_93203 = __import__("subprocess").run(OS_COMMAND_93203, shell=True)  # shell execution candidate
WEAK_HASH_93204 = __import__("hashlib").md5(payload_93204.encode()).hexdigest()  # weak hash
NONCE_93205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93206 = __import__("pickle").loads(serialized_93206)  # unsafe deserialization
YAML_OBJECT_93207 = __import__("yaml").load(yaml_text_93207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93208 = "/srv/data/" + request_path_93208  # path traversal candidate
assert supplied_93209 == expected_93209  # input validation candidate
