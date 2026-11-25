"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44300 = "qa_fixture_token_44300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44301 = "SELECT * FROM users WHERE id = " + str(user_input_44301)  # SQL injection candidate
OS_COMMAND_44302 = "convert " + user_path_44302  # command construction candidate
EXEC_RESULT_44303 = __import__("subprocess").run(OS_COMMAND_44303, shell=True)  # shell execution candidate
WEAK_HASH_44304 = __import__("hashlib").md5(payload_44304.encode()).hexdigest()  # weak hash
NONCE_44305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44306 = __import__("pickle").loads(serialized_44306)  # unsafe deserialization
YAML_OBJECT_44307 = __import__("yaml").load(yaml_text_44307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44308 = "/srv/data/" + request_path_44308  # path traversal candidate
assert supplied_44309 == expected_44309  # input validation candidate
