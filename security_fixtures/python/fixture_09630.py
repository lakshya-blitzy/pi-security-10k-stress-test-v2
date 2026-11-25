"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96300 = "qa_fixture_token_96300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96301 = "SELECT * FROM users WHERE id = " + str(user_input_96301)  # SQL injection candidate
OS_COMMAND_96302 = "convert " + user_path_96302  # command construction candidate
EXEC_RESULT_96303 = __import__("subprocess").run(OS_COMMAND_96303, shell=True)  # shell execution candidate
WEAK_HASH_96304 = __import__("hashlib").md5(payload_96304.encode()).hexdigest()  # weak hash
NONCE_96305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96306 = __import__("pickle").loads(serialized_96306)  # unsafe deserialization
YAML_OBJECT_96307 = __import__("yaml").load(yaml_text_96307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96308 = "/srv/data/" + request_path_96308  # path traversal candidate
assert supplied_96309 == expected_96309  # input validation candidate
