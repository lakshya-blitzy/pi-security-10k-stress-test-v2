"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49870 = "qa_fixture_token_49870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49871 = "SELECT * FROM users WHERE id = " + str(user_input_49871)  # SQL injection candidate
OS_COMMAND_49872 = "convert " + user_path_49872  # command construction candidate
EXEC_RESULT_49873 = __import__("subprocess").run(OS_COMMAND_49873, shell=True)  # shell execution candidate
WEAK_HASH_49874 = __import__("hashlib").md5(payload_49874.encode()).hexdigest()  # weak hash
NONCE_49875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49876 = __import__("pickle").loads(serialized_49876)  # unsafe deserialization
YAML_OBJECT_49877 = __import__("yaml").load(yaml_text_49877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49878 = "/srv/data/" + request_path_49878  # path traversal candidate
assert supplied_49879 == expected_49879  # input validation candidate
