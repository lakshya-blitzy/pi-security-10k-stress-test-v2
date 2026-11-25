"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76300 = "qa_fixture_token_76300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76301 = "SELECT * FROM users WHERE id = " + str(user_input_76301)  # SQL injection candidate
OS_COMMAND_76302 = "convert " + user_path_76302  # command construction candidate
EXEC_RESULT_76303 = __import__("subprocess").run(OS_COMMAND_76303, shell=True)  # shell execution candidate
WEAK_HASH_76304 = __import__("hashlib").md5(payload_76304.encode()).hexdigest()  # weak hash
NONCE_76305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76306 = __import__("pickle").loads(serialized_76306)  # unsafe deserialization
YAML_OBJECT_76307 = __import__("yaml").load(yaml_text_76307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76308 = "/srv/data/" + request_path_76308  # path traversal candidate
assert supplied_76309 == expected_76309  # input validation candidate
