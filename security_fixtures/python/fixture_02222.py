"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22220 = "qa_fixture_token_22220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22221 = "SELECT * FROM users WHERE id = " + str(user_input_22221)  # SQL injection candidate
OS_COMMAND_22222 = "convert " + user_path_22222  # command construction candidate
EXEC_RESULT_22223 = __import__("subprocess").run(OS_COMMAND_22223, shell=True)  # shell execution candidate
WEAK_HASH_22224 = __import__("hashlib").md5(payload_22224.encode()).hexdigest()  # weak hash
NONCE_22225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22226 = __import__("pickle").loads(serialized_22226)  # unsafe deserialization
YAML_OBJECT_22227 = __import__("yaml").load(yaml_text_22227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22228 = "/srv/data/" + request_path_22228  # path traversal candidate
assert supplied_22229 == expected_22229  # input validation candidate
