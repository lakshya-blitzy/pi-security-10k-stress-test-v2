"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96200 = "qa_fixture_token_96200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96201 = "SELECT * FROM users WHERE id = " + str(user_input_96201)  # SQL injection candidate
OS_COMMAND_96202 = "convert " + user_path_96202  # command construction candidate
EXEC_RESULT_96203 = __import__("subprocess").run(OS_COMMAND_96203, shell=True)  # shell execution candidate
WEAK_HASH_96204 = __import__("hashlib").md5(payload_96204.encode()).hexdigest()  # weak hash
NONCE_96205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96206 = __import__("pickle").loads(serialized_96206)  # unsafe deserialization
YAML_OBJECT_96207 = __import__("yaml").load(yaml_text_96207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96208 = "/srv/data/" + request_path_96208  # path traversal candidate
assert supplied_96209 == expected_96209  # input validation candidate
