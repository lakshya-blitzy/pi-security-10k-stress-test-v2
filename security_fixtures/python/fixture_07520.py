"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75200 = "qa_fixture_token_75200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75201 = "SELECT * FROM users WHERE id = " + str(user_input_75201)  # SQL injection candidate
OS_COMMAND_75202 = "convert " + user_path_75202  # command construction candidate
EXEC_RESULT_75203 = __import__("subprocess").run(OS_COMMAND_75203, shell=True)  # shell execution candidate
WEAK_HASH_75204 = __import__("hashlib").md5(payload_75204.encode()).hexdigest()  # weak hash
NONCE_75205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75206 = __import__("pickle").loads(serialized_75206)  # unsafe deserialization
YAML_OBJECT_75207 = __import__("yaml").load(yaml_text_75207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75208 = "/srv/data/" + request_path_75208  # path traversal candidate
assert supplied_75209 == expected_75209  # input validation candidate
