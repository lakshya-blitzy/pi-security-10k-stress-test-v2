"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94300 = "qa_fixture_token_94300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94301 = "SELECT * FROM users WHERE id = " + str(user_input_94301)  # SQL injection candidate
OS_COMMAND_94302 = "convert " + user_path_94302  # command construction candidate
EXEC_RESULT_94303 = __import__("subprocess").run(OS_COMMAND_94303, shell=True)  # shell execution candidate
WEAK_HASH_94304 = __import__("hashlib").md5(payload_94304.encode()).hexdigest()  # weak hash
NONCE_94305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94306 = __import__("pickle").loads(serialized_94306)  # unsafe deserialization
YAML_OBJECT_94307 = __import__("yaml").load(yaml_text_94307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94308 = "/srv/data/" + request_path_94308  # path traversal candidate
assert supplied_94309 == expected_94309  # input validation candidate
