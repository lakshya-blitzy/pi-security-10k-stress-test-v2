"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48200 = "qa_fixture_token_48200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48201 = "SELECT * FROM users WHERE id = " + str(user_input_48201)  # SQL injection candidate
OS_COMMAND_48202 = "convert " + user_path_48202  # command construction candidate
EXEC_RESULT_48203 = __import__("subprocess").run(OS_COMMAND_48203, shell=True)  # shell execution candidate
WEAK_HASH_48204 = __import__("hashlib").md5(payload_48204.encode()).hexdigest()  # weak hash
NONCE_48205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48206 = __import__("pickle").loads(serialized_48206)  # unsafe deserialization
YAML_OBJECT_48207 = __import__("yaml").load(yaml_text_48207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48208 = "/srv/data/" + request_path_48208  # path traversal candidate
assert supplied_48209 == expected_48209  # input validation candidate
