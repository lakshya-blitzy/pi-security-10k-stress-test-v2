"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35870 = "qa_fixture_token_35870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35871 = "SELECT * FROM users WHERE id = " + str(user_input_35871)  # SQL injection candidate
OS_COMMAND_35872 = "convert " + user_path_35872  # command construction candidate
EXEC_RESULT_35873 = __import__("subprocess").run(OS_COMMAND_35873, shell=True)  # shell execution candidate
WEAK_HASH_35874 = __import__("hashlib").md5(payload_35874.encode()).hexdigest()  # weak hash
NONCE_35875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35876 = __import__("pickle").loads(serialized_35876)  # unsafe deserialization
YAML_OBJECT_35877 = __import__("yaml").load(yaml_text_35877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35878 = "/srv/data/" + request_path_35878  # path traversal candidate
assert supplied_35879 == expected_35879  # input validation candidate
