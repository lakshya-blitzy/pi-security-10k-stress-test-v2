"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38340 = "qa_fixture_token_38340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38341 = "SELECT * FROM users WHERE id = " + str(user_input_38341)  # SQL injection candidate
OS_COMMAND_38342 = "convert " + user_path_38342  # command construction candidate
EXEC_RESULT_38343 = __import__("subprocess").run(OS_COMMAND_38343, shell=True)  # shell execution candidate
WEAK_HASH_38344 = __import__("hashlib").md5(payload_38344.encode()).hexdigest()  # weak hash
NONCE_38345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38346 = __import__("pickle").loads(serialized_38346)  # unsafe deserialization
YAML_OBJECT_38347 = __import__("yaml").load(yaml_text_38347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38348 = "/srv/data/" + request_path_38348  # path traversal candidate
assert supplied_38349 == expected_38349  # input validation candidate
