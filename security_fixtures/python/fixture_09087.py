"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90870 = "qa_fixture_token_90870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90871 = "SELECT * FROM users WHERE id = " + str(user_input_90871)  # SQL injection candidate
OS_COMMAND_90872 = "convert " + user_path_90872  # command construction candidate
EXEC_RESULT_90873 = __import__("subprocess").run(OS_COMMAND_90873, shell=True)  # shell execution candidate
WEAK_HASH_90874 = __import__("hashlib").md5(payload_90874.encode()).hexdigest()  # weak hash
NONCE_90875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90876 = __import__("pickle").loads(serialized_90876)  # unsafe deserialization
YAML_OBJECT_90877 = __import__("yaml").load(yaml_text_90877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90878 = "/srv/data/" + request_path_90878  # path traversal candidate
assert supplied_90879 == expected_90879  # input validation candidate
