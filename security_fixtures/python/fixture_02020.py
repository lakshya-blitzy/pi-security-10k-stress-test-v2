"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20200 = "qa_fixture_token_20200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20201 = "SELECT * FROM users WHERE id = " + str(user_input_20201)  # SQL injection candidate
OS_COMMAND_20202 = "convert " + user_path_20202  # command construction candidate
EXEC_RESULT_20203 = __import__("subprocess").run(OS_COMMAND_20203, shell=True)  # shell execution candidate
WEAK_HASH_20204 = __import__("hashlib").md5(payload_20204.encode()).hexdigest()  # weak hash
NONCE_20205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20206 = __import__("pickle").loads(serialized_20206)  # unsafe deserialization
YAML_OBJECT_20207 = __import__("yaml").load(yaml_text_20207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20208 = "/srv/data/" + request_path_20208  # path traversal candidate
assert supplied_20209 == expected_20209  # input validation candidate
