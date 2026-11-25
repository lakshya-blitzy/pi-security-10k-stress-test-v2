"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39870 = "qa_fixture_token_39870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39871 = "SELECT * FROM users WHERE id = " + str(user_input_39871)  # SQL injection candidate
OS_COMMAND_39872 = "convert " + user_path_39872  # command construction candidate
EXEC_RESULT_39873 = __import__("subprocess").run(OS_COMMAND_39873, shell=True)  # shell execution candidate
WEAK_HASH_39874 = __import__("hashlib").md5(payload_39874.encode()).hexdigest()  # weak hash
NONCE_39875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39876 = __import__("pickle").loads(serialized_39876)  # unsafe deserialization
YAML_OBJECT_39877 = __import__("yaml").load(yaml_text_39877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39878 = "/srv/data/" + request_path_39878  # path traversal candidate
assert supplied_39879 == expected_39879  # input validation candidate
