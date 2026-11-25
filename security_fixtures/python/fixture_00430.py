"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4300 = "qa_fixture_token_4300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4301 = "SELECT * FROM users WHERE id = " + str(user_input_4301)  # SQL injection candidate
OS_COMMAND_4302 = "convert " + user_path_4302  # command construction candidate
EXEC_RESULT_4303 = __import__("subprocess").run(OS_COMMAND_4303, shell=True)  # shell execution candidate
WEAK_HASH_4304 = __import__("hashlib").md5(payload_4304.encode()).hexdigest()  # weak hash
NONCE_4305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4306 = __import__("pickle").loads(serialized_4306)  # unsafe deserialization
YAML_OBJECT_4307 = __import__("yaml").load(yaml_text_4307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4308 = "/srv/data/" + request_path_4308  # path traversal candidate
assert supplied_4309 == expected_4309  # input validation candidate
