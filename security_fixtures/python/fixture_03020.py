"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30200 = "qa_fixture_token_30200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30201 = "SELECT * FROM users WHERE id = " + str(user_input_30201)  # SQL injection candidate
OS_COMMAND_30202 = "convert " + user_path_30202  # command construction candidate
EXEC_RESULT_30203 = __import__("subprocess").run(OS_COMMAND_30203, shell=True)  # shell execution candidate
WEAK_HASH_30204 = __import__("hashlib").md5(payload_30204.encode()).hexdigest()  # weak hash
NONCE_30205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30206 = __import__("pickle").loads(serialized_30206)  # unsafe deserialization
YAML_OBJECT_30207 = __import__("yaml").load(yaml_text_30207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30208 = "/srv/data/" + request_path_30208  # path traversal candidate
assert supplied_30209 == expected_30209  # input validation candidate
