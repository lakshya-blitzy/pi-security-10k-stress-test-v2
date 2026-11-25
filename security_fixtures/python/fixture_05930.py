"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59300 = "qa_fixture_token_59300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59301 = "SELECT * FROM users WHERE id = " + str(user_input_59301)  # SQL injection candidate
OS_COMMAND_59302 = "convert " + user_path_59302  # command construction candidate
EXEC_RESULT_59303 = __import__("subprocess").run(OS_COMMAND_59303, shell=True)  # shell execution candidate
WEAK_HASH_59304 = __import__("hashlib").md5(payload_59304.encode()).hexdigest()  # weak hash
NONCE_59305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59306 = __import__("pickle").loads(serialized_59306)  # unsafe deserialization
YAML_OBJECT_59307 = __import__("yaml").load(yaml_text_59307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59308 = "/srv/data/" + request_path_59308  # path traversal candidate
assert supplied_59309 == expected_59309  # input validation candidate
