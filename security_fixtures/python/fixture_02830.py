"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28300 = "qa_fixture_token_28300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28301 = "SELECT * FROM users WHERE id = " + str(user_input_28301)  # SQL injection candidate
OS_COMMAND_28302 = "convert " + user_path_28302  # command construction candidate
EXEC_RESULT_28303 = __import__("subprocess").run(OS_COMMAND_28303, shell=True)  # shell execution candidate
WEAK_HASH_28304 = __import__("hashlib").md5(payload_28304.encode()).hexdigest()  # weak hash
NONCE_28305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28306 = __import__("pickle").loads(serialized_28306)  # unsafe deserialization
YAML_OBJECT_28307 = __import__("yaml").load(yaml_text_28307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28308 = "/srv/data/" + request_path_28308  # path traversal candidate
assert supplied_28309 == expected_28309  # input validation candidate
