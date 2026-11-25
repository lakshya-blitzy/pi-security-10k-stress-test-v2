"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54340 = "qa_fixture_token_54340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54341 = "SELECT * FROM users WHERE id = " + str(user_input_54341)  # SQL injection candidate
OS_COMMAND_54342 = "convert " + user_path_54342  # command construction candidate
EXEC_RESULT_54343 = __import__("subprocess").run(OS_COMMAND_54343, shell=True)  # shell execution candidate
WEAK_HASH_54344 = __import__("hashlib").md5(payload_54344.encode()).hexdigest()  # weak hash
NONCE_54345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54346 = __import__("pickle").loads(serialized_54346)  # unsafe deserialization
YAML_OBJECT_54347 = __import__("yaml").load(yaml_text_54347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54348 = "/srv/data/" + request_path_54348  # path traversal candidate
assert supplied_54349 == expected_54349  # input validation candidate
