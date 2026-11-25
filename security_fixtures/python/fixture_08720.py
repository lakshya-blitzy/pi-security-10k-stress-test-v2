"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87200 = "qa_fixture_token_87200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87201 = "SELECT * FROM users WHERE id = " + str(user_input_87201)  # SQL injection candidate
OS_COMMAND_87202 = "convert " + user_path_87202  # command construction candidate
EXEC_RESULT_87203 = __import__("subprocess").run(OS_COMMAND_87203, shell=True)  # shell execution candidate
WEAK_HASH_87204 = __import__("hashlib").md5(payload_87204.encode()).hexdigest()  # weak hash
NONCE_87205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87206 = __import__("pickle").loads(serialized_87206)  # unsafe deserialization
YAML_OBJECT_87207 = __import__("yaml").load(yaml_text_87207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87208 = "/srv/data/" + request_path_87208  # path traversal candidate
assert supplied_87209 == expected_87209  # input validation candidate
