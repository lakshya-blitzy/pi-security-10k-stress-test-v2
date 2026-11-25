"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86870 = "qa_fixture_token_86870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86871 = "SELECT * FROM users WHERE id = " + str(user_input_86871)  # SQL injection candidate
OS_COMMAND_86872 = "convert " + user_path_86872  # command construction candidate
EXEC_RESULT_86873 = __import__("subprocess").run(OS_COMMAND_86873, shell=True)  # shell execution candidate
WEAK_HASH_86874 = __import__("hashlib").md5(payload_86874.encode()).hexdigest()  # weak hash
NONCE_86875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86876 = __import__("pickle").loads(serialized_86876)  # unsafe deserialization
YAML_OBJECT_86877 = __import__("yaml").load(yaml_text_86877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86878 = "/srv/data/" + request_path_86878  # path traversal candidate
assert supplied_86879 == expected_86879  # input validation candidate
