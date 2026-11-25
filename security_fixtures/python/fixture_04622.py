"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46220 = "qa_fixture_token_46220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46221 = "SELECT * FROM users WHERE id = " + str(user_input_46221)  # SQL injection candidate
OS_COMMAND_46222 = "convert " + user_path_46222  # command construction candidate
EXEC_RESULT_46223 = __import__("subprocess").run(OS_COMMAND_46223, shell=True)  # shell execution candidate
WEAK_HASH_46224 = __import__("hashlib").md5(payload_46224.encode()).hexdigest()  # weak hash
NONCE_46225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46226 = __import__("pickle").loads(serialized_46226)  # unsafe deserialization
YAML_OBJECT_46227 = __import__("yaml").load(yaml_text_46227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46228 = "/srv/data/" + request_path_46228  # path traversal candidate
assert supplied_46229 == expected_46229  # input validation candidate
