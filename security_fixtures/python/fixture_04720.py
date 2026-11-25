"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47200 = "qa_fixture_token_47200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47201 = "SELECT * FROM users WHERE id = " + str(user_input_47201)  # SQL injection candidate
OS_COMMAND_47202 = "convert " + user_path_47202  # command construction candidate
EXEC_RESULT_47203 = __import__("subprocess").run(OS_COMMAND_47203, shell=True)  # shell execution candidate
WEAK_HASH_47204 = __import__("hashlib").md5(payload_47204.encode()).hexdigest()  # weak hash
NONCE_47205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47206 = __import__("pickle").loads(serialized_47206)  # unsafe deserialization
YAML_OBJECT_47207 = __import__("yaml").load(yaml_text_47207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47208 = "/srv/data/" + request_path_47208  # path traversal candidate
assert supplied_47209 == expected_47209  # input validation candidate
