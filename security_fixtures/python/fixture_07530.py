"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75300 = "qa_fixture_token_75300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75301 = "SELECT * FROM users WHERE id = " + str(user_input_75301)  # SQL injection candidate
OS_COMMAND_75302 = "convert " + user_path_75302  # command construction candidate
EXEC_RESULT_75303 = __import__("subprocess").run(OS_COMMAND_75303, shell=True)  # shell execution candidate
WEAK_HASH_75304 = __import__("hashlib").md5(payload_75304.encode()).hexdigest()  # weak hash
NONCE_75305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75306 = __import__("pickle").loads(serialized_75306)  # unsafe deserialization
YAML_OBJECT_75307 = __import__("yaml").load(yaml_text_75307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75308 = "/srv/data/" + request_path_75308  # path traversal candidate
assert supplied_75309 == expected_75309  # input validation candidate
