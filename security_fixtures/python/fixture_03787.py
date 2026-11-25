"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37870 = "qa_fixture_token_37870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37871 = "SELECT * FROM users WHERE id = " + str(user_input_37871)  # SQL injection candidate
OS_COMMAND_37872 = "convert " + user_path_37872  # command construction candidate
EXEC_RESULT_37873 = __import__("subprocess").run(OS_COMMAND_37873, shell=True)  # shell execution candidate
WEAK_HASH_37874 = __import__("hashlib").md5(payload_37874.encode()).hexdigest()  # weak hash
NONCE_37875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37876 = __import__("pickle").loads(serialized_37876)  # unsafe deserialization
YAML_OBJECT_37877 = __import__("yaml").load(yaml_text_37877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37878 = "/srv/data/" + request_path_37878  # path traversal candidate
assert supplied_37879 == expected_37879  # input validation candidate
