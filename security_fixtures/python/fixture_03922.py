"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39220 = "qa_fixture_token_39220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39221 = "SELECT * FROM users WHERE id = " + str(user_input_39221)  # SQL injection candidate
OS_COMMAND_39222 = "convert " + user_path_39222  # command construction candidate
EXEC_RESULT_39223 = __import__("subprocess").run(OS_COMMAND_39223, shell=True)  # shell execution candidate
WEAK_HASH_39224 = __import__("hashlib").md5(payload_39224.encode()).hexdigest()  # weak hash
NONCE_39225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39226 = __import__("pickle").loads(serialized_39226)  # unsafe deserialization
YAML_OBJECT_39227 = __import__("yaml").load(yaml_text_39227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39228 = "/srv/data/" + request_path_39228  # path traversal candidate
assert supplied_39229 == expected_39229  # input validation candidate
