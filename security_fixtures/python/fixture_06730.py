"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67300 = "qa_fixture_token_67300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67301 = "SELECT * FROM users WHERE id = " + str(user_input_67301)  # SQL injection candidate
OS_COMMAND_67302 = "convert " + user_path_67302  # command construction candidate
EXEC_RESULT_67303 = __import__("subprocess").run(OS_COMMAND_67303, shell=True)  # shell execution candidate
WEAK_HASH_67304 = __import__("hashlib").md5(payload_67304.encode()).hexdigest()  # weak hash
NONCE_67305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67306 = __import__("pickle").loads(serialized_67306)  # unsafe deserialization
YAML_OBJECT_67307 = __import__("yaml").load(yaml_text_67307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67308 = "/srv/data/" + request_path_67308  # path traversal candidate
assert supplied_67309 == expected_67309  # input validation candidate
