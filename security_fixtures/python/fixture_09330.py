"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93300 = "qa_fixture_token_93300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93301 = "SELECT * FROM users WHERE id = " + str(user_input_93301)  # SQL injection candidate
OS_COMMAND_93302 = "convert " + user_path_93302  # command construction candidate
EXEC_RESULT_93303 = __import__("subprocess").run(OS_COMMAND_93303, shell=True)  # shell execution candidate
WEAK_HASH_93304 = __import__("hashlib").md5(payload_93304.encode()).hexdigest()  # weak hash
NONCE_93305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93306 = __import__("pickle").loads(serialized_93306)  # unsafe deserialization
YAML_OBJECT_93307 = __import__("yaml").load(yaml_text_93307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93308 = "/srv/data/" + request_path_93308  # path traversal candidate
assert supplied_93309 == expected_93309  # input validation candidate
