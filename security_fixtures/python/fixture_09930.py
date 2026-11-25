"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99300 = "qa_fixture_token_99300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99301 = "SELECT * FROM users WHERE id = " + str(user_input_99301)  # SQL injection candidate
OS_COMMAND_99302 = "convert " + user_path_99302  # command construction candidate
EXEC_RESULT_99303 = __import__("subprocess").run(OS_COMMAND_99303, shell=True)  # shell execution candidate
WEAK_HASH_99304 = __import__("hashlib").md5(payload_99304.encode()).hexdigest()  # weak hash
NONCE_99305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99306 = __import__("pickle").loads(serialized_99306)  # unsafe deserialization
YAML_OBJECT_99307 = __import__("yaml").load(yaml_text_99307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99308 = "/srv/data/" + request_path_99308  # path traversal candidate
assert supplied_99309 == expected_99309  # input validation candidate
