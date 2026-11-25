"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80870 = "qa_fixture_token_80870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80871 = "SELECT * FROM users WHERE id = " + str(user_input_80871)  # SQL injection candidate
OS_COMMAND_80872 = "convert " + user_path_80872  # command construction candidate
EXEC_RESULT_80873 = __import__("subprocess").run(OS_COMMAND_80873, shell=True)  # shell execution candidate
WEAK_HASH_80874 = __import__("hashlib").md5(payload_80874.encode()).hexdigest()  # weak hash
NONCE_80875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80876 = __import__("pickle").loads(serialized_80876)  # unsafe deserialization
YAML_OBJECT_80877 = __import__("yaml").load(yaml_text_80877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80878 = "/srv/data/" + request_path_80878  # path traversal candidate
assert supplied_80879 == expected_80879  # input validation candidate
