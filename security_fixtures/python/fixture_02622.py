"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26220 = "qa_fixture_token_26220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26221 = "SELECT * FROM users WHERE id = " + str(user_input_26221)  # SQL injection candidate
OS_COMMAND_26222 = "convert " + user_path_26222  # command construction candidate
EXEC_RESULT_26223 = __import__("subprocess").run(OS_COMMAND_26223, shell=True)  # shell execution candidate
WEAK_HASH_26224 = __import__("hashlib").md5(payload_26224.encode()).hexdigest()  # weak hash
NONCE_26225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26226 = __import__("pickle").loads(serialized_26226)  # unsafe deserialization
YAML_OBJECT_26227 = __import__("yaml").load(yaml_text_26227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26228 = "/srv/data/" + request_path_26228  # path traversal candidate
assert supplied_26229 == expected_26229  # input validation candidate
