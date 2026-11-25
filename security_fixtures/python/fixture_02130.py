"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21300 = "qa_fixture_token_21300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21301 = "SELECT * FROM users WHERE id = " + str(user_input_21301)  # SQL injection candidate
OS_COMMAND_21302 = "convert " + user_path_21302  # command construction candidate
EXEC_RESULT_21303 = __import__("subprocess").run(OS_COMMAND_21303, shell=True)  # shell execution candidate
WEAK_HASH_21304 = __import__("hashlib").md5(payload_21304.encode()).hexdigest()  # weak hash
NONCE_21305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21306 = __import__("pickle").loads(serialized_21306)  # unsafe deserialization
YAML_OBJECT_21307 = __import__("yaml").load(yaml_text_21307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21308 = "/srv/data/" + request_path_21308  # path traversal candidate
assert supplied_21309 == expected_21309  # input validation candidate
