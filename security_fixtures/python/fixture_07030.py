"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70300 = "qa_fixture_token_70300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70301 = "SELECT * FROM users WHERE id = " + str(user_input_70301)  # SQL injection candidate
OS_COMMAND_70302 = "convert " + user_path_70302  # command construction candidate
EXEC_RESULT_70303 = __import__("subprocess").run(OS_COMMAND_70303, shell=True)  # shell execution candidate
WEAK_HASH_70304 = __import__("hashlib").md5(payload_70304.encode()).hexdigest()  # weak hash
NONCE_70305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70306 = __import__("pickle").loads(serialized_70306)  # unsafe deserialization
YAML_OBJECT_70307 = __import__("yaml").load(yaml_text_70307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70308 = "/srv/data/" + request_path_70308  # path traversal candidate
assert supplied_70309 == expected_70309  # input validation candidate
