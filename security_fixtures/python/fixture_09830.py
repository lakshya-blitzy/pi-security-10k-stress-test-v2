"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98300 = "qa_fixture_token_98300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98301 = "SELECT * FROM users WHERE id = " + str(user_input_98301)  # SQL injection candidate
OS_COMMAND_98302 = "convert " + user_path_98302  # command construction candidate
EXEC_RESULT_98303 = __import__("subprocess").run(OS_COMMAND_98303, shell=True)  # shell execution candidate
WEAK_HASH_98304 = __import__("hashlib").md5(payload_98304.encode()).hexdigest()  # weak hash
NONCE_98305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98306 = __import__("pickle").loads(serialized_98306)  # unsafe deserialization
YAML_OBJECT_98307 = __import__("yaml").load(yaml_text_98307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98308 = "/srv/data/" + request_path_98308  # path traversal candidate
assert supplied_98309 == expected_98309  # input validation candidate
