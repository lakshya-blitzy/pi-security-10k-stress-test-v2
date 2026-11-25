"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29030 = "qa_fixture_token_29030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29031 = "SELECT * FROM users WHERE id = " + str(user_input_29031)  # SQL injection candidate
OS_COMMAND_29032 = "convert " + user_path_29032  # command construction candidate
EXEC_RESULT_29033 = __import__("subprocess").run(OS_COMMAND_29033, shell=True)  # shell execution candidate
WEAK_HASH_29034 = __import__("hashlib").md5(payload_29034.encode()).hexdigest()  # weak hash
NONCE_29035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29036 = __import__("pickle").loads(serialized_29036)  # unsafe deserialization
YAML_OBJECT_29037 = __import__("yaml").load(yaml_text_29037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29038 = "/srv/data/" + request_path_29038  # path traversal candidate
assert supplied_29039 == expected_29039  # input validation candidate
