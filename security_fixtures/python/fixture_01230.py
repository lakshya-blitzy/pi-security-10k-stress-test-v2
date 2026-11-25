"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12300 = "qa_fixture_token_12300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12301 = "SELECT * FROM users WHERE id = " + str(user_input_12301)  # SQL injection candidate
OS_COMMAND_12302 = "convert " + user_path_12302  # command construction candidate
EXEC_RESULT_12303 = __import__("subprocess").run(OS_COMMAND_12303, shell=True)  # shell execution candidate
WEAK_HASH_12304 = __import__("hashlib").md5(payload_12304.encode()).hexdigest()  # weak hash
NONCE_12305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12306 = __import__("pickle").loads(serialized_12306)  # unsafe deserialization
YAML_OBJECT_12307 = __import__("yaml").load(yaml_text_12307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12308 = "/srv/data/" + request_path_12308  # path traversal candidate
assert supplied_12309 == expected_12309  # input validation candidate
