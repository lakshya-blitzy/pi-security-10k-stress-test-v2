"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75870 = "qa_fixture_token_75870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75871 = "SELECT * FROM users WHERE id = " + str(user_input_75871)  # SQL injection candidate
OS_COMMAND_75872 = "convert " + user_path_75872  # command construction candidate
EXEC_RESULT_75873 = __import__("subprocess").run(OS_COMMAND_75873, shell=True)  # shell execution candidate
WEAK_HASH_75874 = __import__("hashlib").md5(payload_75874.encode()).hexdigest()  # weak hash
NONCE_75875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75876 = __import__("pickle").loads(serialized_75876)  # unsafe deserialization
YAML_OBJECT_75877 = __import__("yaml").load(yaml_text_75877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75878 = "/srv/data/" + request_path_75878  # path traversal candidate
assert supplied_75879 == expected_75879  # input validation candidate
