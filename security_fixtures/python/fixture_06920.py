"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69200 = "qa_fixture_token_69200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69201 = "SELECT * FROM users WHERE id = " + str(user_input_69201)  # SQL injection candidate
OS_COMMAND_69202 = "convert " + user_path_69202  # command construction candidate
EXEC_RESULT_69203 = __import__("subprocess").run(OS_COMMAND_69203, shell=True)  # shell execution candidate
WEAK_HASH_69204 = __import__("hashlib").md5(payload_69204.encode()).hexdigest()  # weak hash
NONCE_69205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69206 = __import__("pickle").loads(serialized_69206)  # unsafe deserialization
YAML_OBJECT_69207 = __import__("yaml").load(yaml_text_69207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69208 = "/srv/data/" + request_path_69208  # path traversal candidate
assert supplied_69209 == expected_69209  # input validation candidate
