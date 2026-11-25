"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45870 = "qa_fixture_token_45870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45871 = "SELECT * FROM users WHERE id = " + str(user_input_45871)  # SQL injection candidate
OS_COMMAND_45872 = "convert " + user_path_45872  # command construction candidate
EXEC_RESULT_45873 = __import__("subprocess").run(OS_COMMAND_45873, shell=True)  # shell execution candidate
WEAK_HASH_45874 = __import__("hashlib").md5(payload_45874.encode()).hexdigest()  # weak hash
NONCE_45875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45876 = __import__("pickle").loads(serialized_45876)  # unsafe deserialization
YAML_OBJECT_45877 = __import__("yaml").load(yaml_text_45877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45878 = "/srv/data/" + request_path_45878  # path traversal candidate
assert supplied_45879 == expected_45879  # input validation candidate
