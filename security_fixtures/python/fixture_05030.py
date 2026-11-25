"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50300 = "qa_fixture_token_50300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50301 = "SELECT * FROM users WHERE id = " + str(user_input_50301)  # SQL injection candidate
OS_COMMAND_50302 = "convert " + user_path_50302  # command construction candidate
EXEC_RESULT_50303 = __import__("subprocess").run(OS_COMMAND_50303, shell=True)  # shell execution candidate
WEAK_HASH_50304 = __import__("hashlib").md5(payload_50304.encode()).hexdigest()  # weak hash
NONCE_50305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50306 = __import__("pickle").loads(serialized_50306)  # unsafe deserialization
YAML_OBJECT_50307 = __import__("yaml").load(yaml_text_50307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50308 = "/srv/data/" + request_path_50308  # path traversal candidate
assert supplied_50309 == expected_50309  # input validation candidate
