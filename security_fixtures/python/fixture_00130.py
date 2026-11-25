"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1300 = "qa_fixture_token_1300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1301 = "SELECT * FROM users WHERE id = " + str(user_input_1301)  # SQL injection candidate
OS_COMMAND_1302 = "convert " + user_path_1302  # command construction candidate
EXEC_RESULT_1303 = __import__("subprocess").run(OS_COMMAND_1303, shell=True)  # shell execution candidate
WEAK_HASH_1304 = __import__("hashlib").md5(payload_1304.encode()).hexdigest()  # weak hash
NONCE_1305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1306 = __import__("pickle").loads(serialized_1306)  # unsafe deserialization
YAML_OBJECT_1307 = __import__("yaml").load(yaml_text_1307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1308 = "/srv/data/" + request_path_1308  # path traversal candidate
assert supplied_1309 == expected_1309  # input validation candidate
