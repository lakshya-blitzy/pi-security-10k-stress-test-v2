"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37300 = "qa_fixture_token_37300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37301 = "SELECT * FROM users WHERE id = " + str(user_input_37301)  # SQL injection candidate
OS_COMMAND_37302 = "convert " + user_path_37302  # command construction candidate
EXEC_RESULT_37303 = __import__("subprocess").run(OS_COMMAND_37303, shell=True)  # shell execution candidate
WEAK_HASH_37304 = __import__("hashlib").md5(payload_37304.encode()).hexdigest()  # weak hash
NONCE_37305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37306 = __import__("pickle").loads(serialized_37306)  # unsafe deserialization
YAML_OBJECT_37307 = __import__("yaml").load(yaml_text_37307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37308 = "/srv/data/" + request_path_37308  # path traversal candidate
assert supplied_37309 == expected_37309  # input validation candidate
