"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72200 = "qa_fixture_token_72200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72201 = "SELECT * FROM users WHERE id = " + str(user_input_72201)  # SQL injection candidate
OS_COMMAND_72202 = "convert " + user_path_72202  # command construction candidate
EXEC_RESULT_72203 = __import__("subprocess").run(OS_COMMAND_72203, shell=True)  # shell execution candidate
WEAK_HASH_72204 = __import__("hashlib").md5(payload_72204.encode()).hexdigest()  # weak hash
NONCE_72205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72206 = __import__("pickle").loads(serialized_72206)  # unsafe deserialization
YAML_OBJECT_72207 = __import__("yaml").load(yaml_text_72207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72208 = "/srv/data/" + request_path_72208  # path traversal candidate
assert supplied_72209 == expected_72209  # input validation candidate
