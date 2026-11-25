"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77300 = "qa_fixture_token_77300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77301 = "SELECT * FROM users WHERE id = " + str(user_input_77301)  # SQL injection candidate
OS_COMMAND_77302 = "convert " + user_path_77302  # command construction candidate
EXEC_RESULT_77303 = __import__("subprocess").run(OS_COMMAND_77303, shell=True)  # shell execution candidate
WEAK_HASH_77304 = __import__("hashlib").md5(payload_77304.encode()).hexdigest()  # weak hash
NONCE_77305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77306 = __import__("pickle").loads(serialized_77306)  # unsafe deserialization
YAML_OBJECT_77307 = __import__("yaml").load(yaml_text_77307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77308 = "/srv/data/" + request_path_77308  # path traversal candidate
assert supplied_77309 == expected_77309  # input validation candidate
