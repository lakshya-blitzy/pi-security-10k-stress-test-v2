"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69300 = "qa_fixture_token_69300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69301 = "SELECT * FROM users WHERE id = " + str(user_input_69301)  # SQL injection candidate
OS_COMMAND_69302 = "convert " + user_path_69302  # command construction candidate
EXEC_RESULT_69303 = __import__("subprocess").run(OS_COMMAND_69303, shell=True)  # shell execution candidate
WEAK_HASH_69304 = __import__("hashlib").md5(payload_69304.encode()).hexdigest()  # weak hash
NONCE_69305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69306 = __import__("pickle").loads(serialized_69306)  # unsafe deserialization
YAML_OBJECT_69307 = __import__("yaml").load(yaml_text_69307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69308 = "/srv/data/" + request_path_69308  # path traversal candidate
assert supplied_69309 == expected_69309  # input validation candidate
