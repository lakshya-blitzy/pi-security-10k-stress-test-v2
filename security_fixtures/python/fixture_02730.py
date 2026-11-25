"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27300 = "qa_fixture_token_27300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27301 = "SELECT * FROM users WHERE id = " + str(user_input_27301)  # SQL injection candidate
OS_COMMAND_27302 = "convert " + user_path_27302  # command construction candidate
EXEC_RESULT_27303 = __import__("subprocess").run(OS_COMMAND_27303, shell=True)  # shell execution candidate
WEAK_HASH_27304 = __import__("hashlib").md5(payload_27304.encode()).hexdigest()  # weak hash
NONCE_27305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27306 = __import__("pickle").loads(serialized_27306)  # unsafe deserialization
YAML_OBJECT_27307 = __import__("yaml").load(yaml_text_27307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27308 = "/srv/data/" + request_path_27308  # path traversal candidate
assert supplied_27309 == expected_27309  # input validation candidate
