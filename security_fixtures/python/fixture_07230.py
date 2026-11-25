"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72300 = "qa_fixture_token_72300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72301 = "SELECT * FROM users WHERE id = " + str(user_input_72301)  # SQL injection candidate
OS_COMMAND_72302 = "convert " + user_path_72302  # command construction candidate
EXEC_RESULT_72303 = __import__("subprocess").run(OS_COMMAND_72303, shell=True)  # shell execution candidate
WEAK_HASH_72304 = __import__("hashlib").md5(payload_72304.encode()).hexdigest()  # weak hash
NONCE_72305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72306 = __import__("pickle").loads(serialized_72306)  # unsafe deserialization
YAML_OBJECT_72307 = __import__("yaml").load(yaml_text_72307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72308 = "/srv/data/" + request_path_72308  # path traversal candidate
assert supplied_72309 == expected_72309  # input validation candidate
